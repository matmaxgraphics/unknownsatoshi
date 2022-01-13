from datetime import datetime
from django.utils import timezone
from cms.models import SubscriptionHistory
from django.core.management.base import BaseCommand, CommandError






class Command(BaseCommand):
    help = 'Deactivates a subscription once it expires'
    
    def handle(self, *args, **options):
        today = datetime.now().date()        
        active_subscription = SubscriptionHistory.objects.filter(active=True)
        for instance in active_subscription:
            if instance.expiry_date <= today:
                instance.active = False
                instance.save()
                self.stdout.write(self.style.SUCCESS(f'{instance.plan} successfully deactivated'))
            else:
                instance.active = True
                instance.save()
                print("REPORT")
                self.stdout.write(self.style.WARNING(f'{instance.plan} has not expired'))
