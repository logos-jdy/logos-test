"""GitHub 업로드 연습용: 간단한 로그인 기능 테스트 예제.

실행 방법:
    python qa_test_demo.py

파이썬 기본 라이브러리(unittest)만 사용하므로 추가 설치가 필요하지 않습니다.
"""

import unittest


def login(username, password):
    """연습용 로그인 기능. 실제 서비스와 연결되지 않습니다."""
    if not username:
        return "아이디를 입력하세요."
    if not password:
        return "비밀번호를 입력하세요."
    if username == "testuser" and password == "1234":
        return "로그인 성공"
    return "아이디 또는 비밀번호가 올바르지 않습니다."


class LoginTests(unittest.TestCase):
    def test_correct_login(self):
        self.assertEqual(login("testuser", "1234"), "로그인 성공")

    def test_wrong_password(self):
        self.assertEqual(
            login("testuser", "wrong"),
            "아이디 또는 비밀번호가 올바르지 않습니다.",
        )

    def test_wrong_username(self):
        self.assertEqual(
            login("unknown", "1234"),
            "아이디 또는 비밀번호가 올바르지 않습니다.",
        )

    def test_empty_username(self):
        self.assertEqual(login("", "1234"), "아이디를 입력하세요.")

    def test_empty_password(self):
        self.assertEqual(login("testuser", ""), "비밀번호를 입력하세요.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
