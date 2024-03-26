import qrcode  #큐알코드 라이브러리

sk = "https://www.instagram.com/syukaworld/"
qr = qrcode.make(sk)
qr.save('./shoe.png')