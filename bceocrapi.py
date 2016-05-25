# coding: utf-8
from credential import BceCredentials
import time
import requests
import json


class BceOCRAPI(object):
    OCR_HOST = 'ocr.bj.baidubce.com'
    OCR_PORT = 80
    API_PROTOCOL = 'http'
    RECOGNIZE_TEXT_API = '/v1/recognize/text'
    RECOGNIZE_CHARACTER_API = '/v1/recognize/character'
    RECOGNIZE_LINE_API = '/v1/recognize/line'
    SUPPORT_LANG = ('CHN_ENG', 'ENG')

    def __init__(self, access_token, secret_token):
        self.credentials = BceCredentials(access_token, secret_token)

    def _get_url(self, path):
        return '{}://{}{}'.format(self.API_PROTOCOL, self.OCR_HOST, path)

    def _buld_headers(self, path, content):
        # Get current timestamp and UTC format for this timestamp
        timestamp = time.time()
        bceDate = self.credentials.get_canonical_time(timestamp)
        headers = {
            "host": self.OCR_HOST,
            "content-type": 'application/json',
            "x-bce-date": bceDate
        }
        authorization = self._get_authorization_str(headers, path, content, timestamp)
        headers['authorization'] = authorization
        return headers

    def _get_authorization_str(self, headers, path, content, timestamp):
        http_method = "POST"
        result = self.credentials.sign(http_method, path, headers, None, timestamp, headers_to_sign={"host", "x-bce-date"})
        return result

    def _recognize_line_or_text(self, api_path, content, language):
        api_url = self._get_url(api_path)
        headers = self._buld_headers(api_path, content)
        r = requests.post(
            url=api_url,
            headers=headers,
            data=json.dumps({'base64': content, 'language': language})
        )
        ocr_result = r.json()
        text = ''
        if ocr_result.has_key('results'):
            for obj in ocr_result['results']:
                text += u'{}\n'.format(obj['word'])

            return text
        else:
            return "no results"

    def get_ocr_text(self, content, language='CHN_ENG'):
        """
        Call BCE OCR API to recognize all the text in the image.
        :calls: `POST /v1/recognize/text`
        :param content: string, (required), base64 encode string of the image data
        :param language: string, (required), text language in the image
        :rtype: OCR recognize text
        """
        assert isinstance(content, (str, unicode)), 'content should be str/unicode'
        assert isinstance(language, (str, unicode)) and language in (self.SUPPORT_LANG), 'language should be in {}'.format(','.join(self.SUPPORT_LANG))
        return self._recognize_line_or_text(self.RECOGNIZE_TEXT_API, content, language)

    def get_ocr_line(self, content, language='CHN_ENG'):
        """
        Call BCE OCR API to recognize single line of text in the image.
        :calls: `POST /v1/recognize/text`
        :param content: string, (required), base64 encode string of the image data
        :param language: string, (required), text language in the image
        :rtype: OCR recognize text
        """
        assert isinstance(content, (str, unicode)), 'content should be str/unicode'
        assert isinstance(language, (str, unicode)) and language in (self.SUPPORT_LANG), 'language should be in {}'.format(','.join(self.SUPPORT_LANG))
        return self._recognize_line_or_text(self.RECOGNIZE_LINE_API, content, language)

    def get_ocr_char(self, content, language='CHN_ENG'):
        """
        Call BCE OCR API to recognize single char in the image.
        :calls: `POST /v1/recognize/text`
        :param content: string, (required), base64 encode string of the image data
        :param language: string, (required), text language in the image
        :rtype: OCR recognize text
        """
        assert isinstance(content, (str, unicode)), 'content should be str/unicode'
        assert isinstance(language, (str, unicode)) and language in (self.SUPPORT_LANG), 'language should be in {}'.format(','.join(self.SUPPORT_LANG))
        headers = self._buld_headers(self.RECOGNIZE_CHARACTER_API, content)
        api_url = self._get_url(self.RECOGNIZE_CHARACTER_API)
        r = requests.post(
            url=api_url,
            headers=headers,
            data=json.dumps({'base64': content, 'language': language})
        )
        ocr_result = r.json()
        text = ''
        for char in ocr_result['results']:
            text += u'{}\n'.format(char['word'])

        return text