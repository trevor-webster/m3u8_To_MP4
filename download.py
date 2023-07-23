
import m3u8_To_MP4.__init__
from m3u8_To_MP4.__init__ import multithread_download, download

mp4_file_name='M1_L2: The Functions of Eg.mp4'


download(m3u8_uri='https://cfvod.kaltura.com/scf/hls/p/3162383/sp/316238300/serveFlavor/entryId/1_mbcyux8d/v/1/ev/4/flavorId/1_23g3zo0r/name/a.mp4/index.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZnZvZC5rYWx0dXJhLmNvbS9zY2YvaGxzL3AvMzE2MjM4My9zcC8zMTYyMzgzMDAvc2VydmVGbGF2b3IvZW50cnlJZC8xX21iY3l1eDhkL3YvMS9ldi80KiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY5MDIxMTQzN319fV19&Signature=GMGGiI3hB1m43hP-4djXDvqOWpJ6PtQv85ycH5Ts5aNi90lwUwT~bnDgx5XUC-3iwNbw5dcuBBZD8uL49AHpCpuFxb67qUnpn0yRu6STBiJhH0VagoLSne1V~3DzByywJVw1NoEX053lL-ZHD~49RS-YpRlKM8siErzgypNRFFAyFfPzU05sItrrsbdbML8p39vtkvwhZiYlWi3tZvuSOKpROC7UYtu~PQs-juFx4T1AE8xDtw~YwMMFbsh6mNFVOKwesfVDsRSvp1AsTYQXKVOtRl9nY0Sb-Q1n4QpaGpXM-Uw8Yu3B56zT2uj1CxWYhbCTjSWDzIX16OZitMEx2g__&Key-Pair-Id=APKAJT6QIWSKVYK3V34A',
         mp4_file_name=mp4_file_name,         
)

# multithread_download('https://cfvod.kaltura.com/scf/hls/p/3162383/sp/316238300/serveFlavor/entryId/1_kt4gkml2/v/1/ev/3/flavorId/1_tqmrcr28/name/a.mp4/index.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZnZvZC5rYWx0dXJhLmNvbS9zY2YvaGxzL3AvMzE2MjM4My9zcC8zMTYyMzgzMDAvc2VydmVGbGF2b3IvZW50cnlJZC8xX2t0NGdrbWwyL3YvMS9ldi8zKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4OTExNDQwOX19fV19&Signature=Kw3UmjrEX-lq2FVpWXICqoWMkxi9qXRB7N4TVRcEMxPJQat1DS03imV7ccASlJrtOgotodFc-nDzc-qWiRRBoaKR2I7YX9MKHIqaNPEtGlIuVvyn0JXFZa0Akojlxm~DrQ9kBFFO9r4PCxmo1TlzotLPadm-Xtq5BJBM2k77L4qAAQbrG1MC9ekM88AeAiDyKz4-Souy1bEGvtUreHLZZ7jtXzxlIq~UIfx~2WEVXj1cWiPDkN8WZFw558NY4rZj3zNwUrC2ywOFG6dnSl2iszsc1aYvl7-BVqa2LtTeilCuJAzpf82~5OaWSLj-xoDRL-XJpfjlyRHcevq1Dvd0Lg__&Key-Pair-Id=APKAJT6QIWSKVYK3V34A', 
#                      file_path=file_path,
#                      tmp_file_name='a.mp4')

    # 2. Download videos from existing m3u8 files.
    # m3u8_To_MP4.multithread_file_download('http://videoserver.com/playlist.m3u8',m3u8_file_path)

    # For compatibility, i reserve this api, but i do not recommend to you again.
    # m3u8_To_MP4.download('http://videoserver.com/playlist.m3u8')