class Settings:
    """"""
    
    # Default settings
    DEBUG      = True
    PORT       = 8000
    TESTING    = True
    HOST       = '127.0.0.1'
    SECRET_KEY = 'test'
    
    # Cookies
    SESSION_COOKIE_NAME        = 'test'
    SESSION_COOKIE_HTTPONLY    = True
    SESSION_COOKIE_SECURE      = False
    PERMANENT_SESSION_LIFETIME = 3600
