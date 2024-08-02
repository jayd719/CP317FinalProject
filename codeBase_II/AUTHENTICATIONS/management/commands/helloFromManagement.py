from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Prints Hello, World!'

    def handle(self, *args, **kwargs):
        self.stdout.write("Hello, World!")
        
        
class Command(BaseCommand):
    help= "BASE COMMAND"
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stderr.write("s")
        self.stdout.write("Hello Word ")