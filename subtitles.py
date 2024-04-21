import pysubs2 as ps2


class SubtitleError(Exception):
    pass


class SubtitleFile:
    def __init__(self, path: str) -> None:
        self.path = path
        self.subs = ps2.load(path)

    def get_style(self, target: str = "Default") -> ps2.SSAStyle:
        '''
        Returns the style asked for, defaults to "Default"
        '''
        return self.subs.styles[target]

    def set_style(self, target: str = "Default", replacement: ps2.SSAStyle = None) -> None:
        '''
        Replaces the target style with the replacement style, raises SubtitleError if no replacement style is provided.
        Default target is "Default"
        '''
        if replacement:
            self.subs.styles[target] = replacement
        else:
            raise SubtitleError("No replacement style provided")

    def save(self, output_path: str) -> None:
        '''
        Saves the subtitle file to specified output_path.
        '''
        self.subs.save(output_path)
