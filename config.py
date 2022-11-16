
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

## Enter your Open API Key here
OPENAI_API_KEY = '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'
