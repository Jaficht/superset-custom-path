SESSION_COOKIE_SAMESITE = None
ENABLE_PROXY_FIX = True
PUBLIC_ROLE_LIKE_GAMMA = True
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "EMBEDDED_SUPERSET": True
}

SECRET_KEY = 'siaciwelanlnaisnleiwqbeqowbcekwhb3q43r3525fsrdfqw3ccq3'

CORS_OPTIONS = {
  'supports_credentials': True,
  'allow_headers': ['*'],
  'resources':['*'],
  'origins': ['*']
}

GUEST_ROLE_NAME = "Gamma"
GUEST_TOKEN_JWT_SECRET = "nxjNCLanlkcsdnLKDNSA32RD23CVREACvsacecas4344f0000002e"
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_HEADER_NAME = "X-GuestToken"
GUEST_TOKEN_JWT_EXP_SECONDS = 3600  # 1 hour

TALISMAN_ENABLED = False 
