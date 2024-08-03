from typing import Any
from django.core.management.base import BaseCommand
from time import sleep


class Command(BaseCommand):
    """
    -------------------------------------------------------
    Custom Django management command that writes messages to the console.
    It repeatedly writes "Hello World" to stdout and uses stderr to write a specified text.
    Use: python manage.py <command_name>
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        None
    -------------------------------------------------------
    """
    help= "BASE COMMAND"
    text_ = f'Results From {__name__}'
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        """
        -------------------------------------------------------
        Executes the main logic of the command. Writes a message to stderr, then
        repeatedly writes "Hello World" to stdout 10 times with a 0.5-second interval.
        Finally, calls a secondary function to write another message to stderr.
        Use: manage.py <command_name>
        -------------------------------------------------------
        Parameters:
            *args - Positional arguments passed to the command (Any).
            **options - Keyword arguments passed to the command (Any).
        Returns:
            str or None - The return type of the function (str | None).
        -------------------------------------------------------
        """
        self.stderr.write(self.text_)
        i=0
        while(i<10):
            self.stdout.write("Hello Word ")
            sleep(.5)
            i+=1
        
        
        self.newFunction()
        
    # def handle(self, *args, **kwargs):
    #     self.stdout.write("Hello Word Just sfasfOne")
    
    def newFunction(self):
        self.stderr.write(self.text_)