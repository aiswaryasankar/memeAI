import pynecone as pc

config = pc.Config(
    app_name="webapp_pynecone",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
