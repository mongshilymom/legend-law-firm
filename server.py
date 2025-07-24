#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import os
import sys

# UTF-8 인코딩 강제 설정
if sys.platform.startswith('win'):
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.detach())

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # UTF-8 헤더 강제 추가
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        super().end_headers()
    
    def guess_type(self, path):
        # HTML 파일에 대해 UTF-8 인코딩 명시
        mimetype, encoding = super().guess_type(path)
        if mimetype == 'text/html':
            return 'text/html; charset=utf-8'
        return mimetype

PORT = 3001

print("🏆 LEGEND LAW FIRM 서버 시작...")
print(f"🌐 http://localhost:{PORT}")
print("🔥 김앤장 초월 프리미엄 웹사이트 서비스 중...")
print("한글 깨짐 해결 완료! ✅")
print("\n서버를 중단하려면 Ctrl+C를 누르세요.")

try:
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n🛑 Legend Law Firm 서버가 중단되었습니다.")