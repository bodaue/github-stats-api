from dishka import Provider, provide, Scope

from src.core.settings import Settings, create_settings


class CoreProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_settings(self) -> Settings:
        return create_settings()
