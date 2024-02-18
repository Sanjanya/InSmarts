import firebase_admin
from firebase_admin import credentials

# Replace the following lines with your actual Firebase configuration
FIREBASE_CONFIG = {
    "type": "service_account",
    "project_id": "insmarts-ca6eb",
    "private_key_id": "802eef073e34268ef6bbc47060147311944859ec",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDy2BNpdSg1vKpa\n+TpJB6izCfAK+Oh8if0pnjzSPvKx4M/QyBQatAMfsGTj58UOOe2gVTcT/LUzDcTO\n5EDm0CHLMjZtZqFzMK9iYpdqDTWI6+NkLDYBT9/1h5R/jJOGnjnvFsPnF0UGhOOJ\nBkfnNHRuspBCi+/90xHNHhqAWH9Tq4yAgOa7UcTRK8RGJKHWFEXiOl80fjLfPuY1\nXL1f0pKwOwmobQs1B/X49X2ya/2Hyl2b9MjlrMhPzkM43ot/Rj5b2ktghyAL1t17\n0FpARyZ+bHMdE8mSniJETSYJ30UQccvpUEnAT4armo1gcTycaGavTcSFWajhcGpc\ndW0XzrDBAgMBAAECggEAAa+2X6eRuuDxxgy9zbKGvWqxAAMT2DppzC9whC+t70Y4\nEPEiLcAB6WcsgVPxKvuopHZ/mc9lVk4aWeHhrxHKJ24wA6SLxkJmLxtUGBB56xa+\n1fdtDwLGGEPc3wZPNT4A+aG/KSogz3m+ROc4gz+xd7l4E32oEgbrT8NNk09g39Xk\ntckqhbY2jUpcONrLdKHHCt+Ncgmm+BEZwWWQk6vjYWsYcXGb7aIcCDj2cmrBmSep\nxq1aerOQ2xhghjPis9efu8Rw24YTYiqLy/Adndrq/9Kl8Q5TVd+/XRpl+cyda4X+\ndDR2jjc/CVSGS8RRsOhKbR98QEFlgnUxyXAhsLW7jQKBgQD75wd4oQYA8AHlCSZU\nQJFQW7CiS7842/wDSqcmWRYtURor9kiLRgEHpygvUuLHRC3DTfaTPiX1jNNQx3UP\nH5p9bmIQo7X+qloDiy9id81YAjcoETdz3bQOS5h6GPnebcuAk/y+EnweSP4BD+C5\n5dzYmfYgf8joNOk1E2KdglvVBQKBgQD2y1NeOGsTsWZqIu2I3nxpiaijFWkCkXSb\neu6orDE6Jb8MSAVQASqtcdj7tmOTaJwt85kSU4wihtJrb+p5K/9769Mf0UkTlXqK\nt1Kbv+XzHQqyArCziGO/KE+eEYz8AMbkYiuFgufbiQIhPBGb6yEng9LmcVKbgpEn\nyokgO095jQKBgEIKufy4SrioM/b2RSRFoVNuFosWTNX9Zr7+LYByTswmvTPVaAOL\noO1+t5xgoLAZgd34bLMB0jXka+p7wIbshDZqYC94nFheFSdksFGikyWFvyw0B1PL\nRk+RJjKspaXZJ0dYhSTX986A2IcywHo8d4AaLVsr5WJrrNCLeolNCgJ5AoGBAMRM\nteMbvQ/M60lAvu8/CHZpqFkPjpccW0PQZESFsiIuI+gA4TjhtLCA/bY5PLrjWlay\ni+6nxa8wze3m9vmqpWxMB4InVZjeLLppVqvL13uofflZanNi6PQDfFCeZSWM+KZv\n724i0YktUSReQyNhwt1LXVUujiZjlFGyJ6AbjPuBAoGBAOWCf7uIYWFkNk/YJW+O\nKR+3uBW1qBlPCcbJFWhXbFRpYWWgwWpeuNa8YM6eQzkP9NLyH0MbbO6TqUtW3mW3\nMmsJ4HRIFzqCB5+QX2zY+my0Lh32BARkMzHNvB2FPN8laeQxcS12h8RPIdClBcDt\nP+BcrgUb/NBA6nmS1NSLu1vY\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-xjga2@insmarts-ca6eb.iam.gserviceaccount.com",
    "client_id": "104795454125053293599",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xjga2%40insmarts-ca6eb.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# Initialize the Firebase SDK
cred = credentials.Certificate(FIREBASE_CONFIG)
firebase_admin.initialize_app(cred)