# noqa: E111
import unittest
import backup
import json
from unittest.mock import patch
from datetime import date


class Test(unittest.TestCase):
  def test_validate_json_without_bucket_name(self):
    with self.assertRaises(SystemExit) as cm:
      backup.validate_json({"bucket_name": ""})

    self.assertEqual(cm.exception.code, 1)

  def test_validate_json_with_bucket_name(self):
    actual = backup.validate_json({"bucket_name": "test_bucket_name"})
    expected = {"bucket_name": "test_bucket_name"}
    self.assertEqual(actual, expected)

  def test_get_curl_str(self):
    actual = backup.get_curl_str("| curl_str", "www.google.com", "bucket_name", "file_name.txt")
    expected = "curl www.google.com | curl_str | aws s3 cp - \"s3://bucket_name/file_name.txt\" --storage-class DEEP_ARCHIVE"
    self.assertEqual(actual, expected)

  def test_get_encrypt_str(self):
    actual = backup.get_encrypt_str("test@gmail.com", "file_name.txt")
    expected = "| gpg --encrypt -r test@gmail.com --trust-model always --output file_name.txt"

    self.assertEqual(actual, expected)

  @patch('backup.get_encrypt_str')
  @patch('backup.get_curl_str')
  @patch('os.system')
  def test_save_files(self, mock_sys, mock_get_curl_str, mock_get_encrypt_str):
    mock_sys.return_value = ""
    mock_get_encrypt_str.return_value = ""
    mock_get_curl_str.return_value = "curl_str"

    actual = backup.save_files("google", "tgz", ["1", "2"], "test@gmail.com", "bucket_name")
    expected = "curl_str && curl_str"
    self.assertEqual(actual, expected)

  @patch("json.load")
  @patch("builtins.open")
  @patch('os.system')
  def test_integration_test(self, mock_sys, mock_open, mock_json_load):
    data = """{
      "bucket_name": "bucket_name",
      "gpg_email": "gpg@gmail.com",
      "facebook_fmt": "zip",
      "facebook_links": ["www.facebook.com/0", "www.facebook.com/1"],
      "google_links": ["www.google.com/0", "www.google.com/1"],
      "google_fmt": "tgz"
    }"""

    mock_sys.return_value = ""
    mock_open.return_value = ""
    mock_json_load.return_value = json.loads(data)

    actual = backup.main()

    expected = {
      "google": f'curl www.google.com/0 | gpg --encrypt -r gpg@gmail.com --trust-model always --output google_{date.today()}_0.tgz | aws s3 cp - "s3://bucket_name/google_{date.today()}_0.tgz" --storage-class DEEP_ARCHIVE && curl www.google.com/1 | gpg --encrypt -r gpg@gmail.com --trust-model always --output google_{date.today()}_1.tgz | aws s3 cp - "s3://bucket_name/google_{date.today()}_1.tgz" --storage-class DEEP_ARCHIVE',  # noqa: E501
      "facebook": f'curl www.facebook.com/0 | gpg --encrypt -r gpg@gmail.com --trust-model always --output facebook_{date.today()}_0.zip | aws s3 cp - "s3://bucket_name/facebook_{date.today()}_0.zip" --storage-class DEEP_ARCHIVE && curl www.facebook.com/1 | gpg --encrypt -r gpg@gmail.com --trust-model always --output facebook_{date.today()}_1.zip | aws s3 cp - "s3://bucket_name/facebook_{date.today()}_1.zip" --storage-class DEEP_ARCHIVE'  # noqa: E501
    }
    self.assertEqual(actual, expected)
