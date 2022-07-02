
from celery import Task
from django.db import transaction


class TransactionTask(Task):
    def transaction_delay(self, *args, **kwargs):

        def d():
            return self.delay(*args, **kwargs)

        return transaction.on_commit(d)
