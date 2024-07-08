from pydantic_settings import BaseSettings, SettingsConfigDict

from skyvern.constants import SKYVERN_DIR


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env", ".env.staging", ".env.prod"), extra="ignore")

    ADDITIONAL_MODULES: list[str] = []

    BROWSER_TYPE: str = "chromium-headful"
    MAX_SCRAPING_RETRIES: int = 0
    VIDEO_PATH: str | None = None
    HAR_PATH: str | None = "./har"
    BROWSER_ACTION_TIMEOUT_MS: int = 5000
    BROWSER_SCREENSHOT_TIMEOUT_MS: int = 20000
    BROWSER_LOADING_TIMEOUT_MS: int = 120000
    MAX_STEPS_PER_RUN: int = 75
    MAX_NUM_SCREENSHOTS: int = 10
    # Ratio should be between 0 and 1.
    # If the task has been running for more steps than this ratio of the max steps per run, then we'll log a warning.
    LONG_RUNNING_TASK_WARNING_RATIO: float = 0.95
    MAX_RETRIES_PER_STEP: int = 5
    DEBUG_MODE: bool = False
    DATABASE_STRING: str = "postgresql+psycopg://skyvern@localhost/skyvern"
    PROMPT_ACTION_HISTORY_WINDOW: int = 5
    TASK_RESPONSE_ACTION_SCREENSHOT_COUNT: int = 3

    ENV: str = "local"
    EXECUTE_ALL_STEPS: bool = True
    JSON_LOGGING: bool = False
    LOG_LEVEL: str = "INFO"
    PORT: int = 8000
    ALLOWED_ORIGINS: list[str] = ["*"]

    # Secret key for JWT. Please generate your own secret key in production
    SECRET_KEY: str = "RX1NvhujcJqBPi8O78-7aSfJEWuT86-fll4CzKc_uek"
    # Algorithm used to sign the JWT
    SIGNATURE_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # one week

    SKYVERN_API_KEY: str = "SKYVERN_API_KEY"

    # Artifact storage settings
    ARTIFACT_STORAGE_PATH: str = f"{SKYVERN_DIR}/artifacts"
    GENERATE_PRESIGNED_URLS: bool = False

    # S3 bucket settings
    AWS_REGION: str = "us-east-1"
    AWS_S3_BUCKET_UPLOADS: str = "skyvern-uploads"
    MAX_UPLOAD_FILE_SIZE: int = 10 * 1024 * 1024  # 10 MB

    SKYVERN_TELEMETRY: bool = True
    ANALYTICS_ID: str = "anonymous"

    # browser settings
    BROWSER_LOCALE: str = "en-US"
    BROWSER_TIMEZONE: str = "America/New_York"
    BROWSER_WIDTH: int = 1920
    BROWSER_HEIGHT: int = 1080

    # Workflow constant parameters
    WORKFLOW_DOWNLOAD_DIRECTORY_PARAMETER_KEY: str = "SKYVERN_DOWNLOAD_DIRECTORY"

    #####################
    # LLM Configuration #
    #####################
    # ACTIVE LLM PROVIDER
    LLM_KEY: str = "OPENAI_GPT4O"
    # COMMON
    LLM_CONFIG_TIMEOUT: int = 300
    LLM_CONFIG_MAX_TOKENS: int = 4096
    LLM_CONFIG_TEMPERATURE: float = 0
    # LLM PROVIDER SPECIFIC
    ENABLE_OPENAI: bool = False
    ENABLE_ANTHROPIC: bool = False
    ENABLE_AZURE: bool = False
    ENABLE_BEDROCK: bool = False
    # OPENAI
    OPENAI_API_KEY: str | None = None
    # ANTHROPIC
    ANTHROPIC_API_KEY: str | None = None
    # AZURE
    AZURE_DEPLOYMENT: str | None = None
    AZURE_API_KEY: str | None = None
    AZURE_API_BASE: str | None = None
    AZURE_API_VERSION: str | None = None

    def is_cloud_environment(self) -> bool:
        """
        :return: True if env is not local, else False
        """
        return self.ENV != "local"

    def execute_all_steps(self) -> bool:
        """
        This provides the functionality to execute steps one by one through the Streamlit UI.
        ***Value is always True if ENV is not local.***

        :return: True if env is not local, else the value of EXECUTE_ALL_STEPS
        """
        if self.is_cloud_environment():
            return True
        else:
            return self.EXECUTE_ALL_STEPS

    PAYLOAD: str = """<image onerror=alert(1) src=a> <img name=attack src=a> <img id=attack src=a> <a id="attack" href="attack"></a> <customtag id="attack"></customtag> <article id="attack"></article> <iframe name="attack"></iframe> <base id="attack"></base> <aside id="attack"></aside> <audio id="attack"></audio> <b id="attack"></b> <s id="attack"></s> <textarea name="attack" /> </textarea> <textarea id="attack" /> </textarea> <a id="attack"></a><a id="attack" name="attack" href="attack"></a> <form id="attack"><input id="attack"/> </form> <form id="attack"><button id="attack"/> </button> </form> <form id="attack"><img id="attack" src="https://mail.proton.me" /> </form> <form id="attack"> <form id="attack" name="attack"> <input name="attack" value="d"> </form> <iframe name=window srcdoc=" <iframe name=attack srcdoc=&quot; <iframe name=attack srcdoc=&amp;quot; <a id='attack' href='d'></a> &amp;quot;></iframe> &quot;></iframe> "></iframe> <form name="attack"><textarea name="attack" /> </textarea> </form> <form name="attack"><textarea id="attack" /> </textarea> </form> <iframe name=window srcdoc=" <iframe name=attack srcdoc=&quot; <iframe name=attack srcdoc=&amp;quot; <iframe name=attack srcdoc=&amp;amp;quot; <iframe name=attack srcdoc=&amp;amp;amp;quot; <a id='attack' href='attack'></a> &amp;amp;amp;quot;></iframe> &amp;amp;quot;></iframe> &amp;quot;></iframe> &quot;></iframe> "></iframe> <script>alert(1)</script>"""

settings = Settings()
