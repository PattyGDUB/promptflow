class Hello:
    def __init__(self, words: list) -> None:
        self.words = words

    def __call__(self, text: str) -> str:
        return f"Hello {','.join(self.words)} {text}!"
