from dataclasses import dataclass

from environs import Env


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    proxy: str
    admin_ids: int
    admin_chat: int
    Lilia_id: int
    use_redis: bool


@dataclass
class Miscellaneous:
    openAI_token: str
    open_weather_token: str
    restriction_id: int
    msg_to_delete: int
    uptime: int
    resend_chat_id: int
    gpt_messager: int
    deafoult_chat_id: int


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            proxy=env.str("BOT_PROXY"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            Lilia_id=env.int("LILIA_ID"),
            use_redis=env.bool("USE_REDIS"),
            admin_chat=env.int("ADMIN_CHAT_ID")
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        misc=Miscellaneous(
            openAI_token=env.str('OPENAI_TOKEN'),
            open_weather_token=env.str('OPEN_WEATHER_TOKEN'),
            restriction_id=-111111,
            msg_to_delete=55555,
            uptime = None,
            resend_chat_id=env.str('RESEND_ID'),
            gpt_messager = 0,
            deafoult_chat_id=env.str('DEAFOULT_CHAT_ID')
        )
    )
