import re

from .base_linter import BaseLinter

CONFIG = {
    'language': 'SCSS',
    'executable': 'scss',
    'lint_args': ['-c', '-C']
}


class Linter(BaseLinter):
    def parse_errors(self, view, errors, lines, errorUnderlines, violationUnderlines, warningUnderlines, errorMessages, violationMessages, warningMessages):
        for match in re.findall(r'^Syntax error:(?P<error>[^\n]+)\n\s+on line (?P<line>\d+)', errors, re.MULTILINE):
            error, line = match
            self.add_message(int(line), lines, error, errorMessages)
