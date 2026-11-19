#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HER SANİYE BİR FELSEFE ÜRETEN MAKİNE
Dünyanın en gereksiz ama en çalışan yazılımı.
Ctrl+C ile durdur, yoksa sonsuza kadar düşünür.
"""

import time
import random
import base64  # gizli bir şey için, merak etme

FELSEFELER = [
    "Var olmak, aslında var olmamaya çalışmaktır.",
    "Kedi masaya çıktığında fizik kanunları istifa eder.",
    "Zamanın geçmesi, senin geçmemendir.",
    "Bir bardak çay demlenirken evren nefesini tutar.",
    "Bilgisayar açıldığında aslında sen kapanırsın.",
    "Sonsuzluk, sadece yeterince uzun beklediğin yerdir.",
    "Miyavlamak, dilin en saf formudur.",
    "Hata 404: Anlam bulunamadı. Ama aramaya devam et.",
    "Her saniye bir öncekini iptal eder.",
    "Bu cümle yanlıştır. Ya da değildir. Kararın senin.",
]

def gizli_mesaj():
    # Saklı siyasi espri (base64 ile gizlenmiş, decode etmeye çalışma)
    gizli = "SSdiYXJ0YWdlbiBpemxlcml5b3Iu"  # "I'm hungry" gibi ama değil, aslında hiçbir şey
    try:
        return base64.b64decode(gizli).decode('utf-8')
    except:
        return "Gizli mesaj yok, sadece şaka."

def felsefe_uret():
    secim = random.choice(FELSEFELER)
    # Ara sıra gizliyi karıştır ama gösterme
    if random.random() < 0.01:  # %1 ihtimalle gizli şeyi düşün
        _ = gizli_mesaj()  # çağır ama kullanma, gizli kalsın
    return secim

def main():
    print("=== HER SANİYE BİR FELSEFE ÜRETEN MAKİNE AKTİF ===")
    print("Durdurmak için Ctrl+C. Yoksa sonsuza kadar düşünürsün.")
    print("-" * 50)
    try:
        while True:
            print(felsefe_uret())
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMakine sustu. Felsefe bitti. (Geçici olarak)")

if __name__ == "__main__":
    main()
