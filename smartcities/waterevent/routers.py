class IntegrationDatabaseRouter(object):
    """
    A router to control all database operations on models in
    the myapp2 application
    """

    def db_for_read(self, model, **hints):
        """
        Point all operations on myapp2 models to 'my_db_2'
        """
        if model._meta.app_label == 'integrate':
            return 'Integration'
        elif model._meta.app_label == 'watershed':
            return 'Watershed'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'integrate':
            return 'Integration'
        elif model._meta.app_label == 'watershed':
            return 'Watershed'
        return 'default'

    def allow_syncdb(self, db, model):
        """
        Make sure the 'myapp2' app only appears on the 'other' db
        """
        if model._meta.app_label == 'integrate':
            return 'Integration'
        elif model._meta.app_label == 'watershed':
            return 'Watershed'
        return 'default'

    # def allow_relation(self, obj1, obj2, **hints):
    #     app_list = ('watershed', 'stormwater', 'integrate')
    #     if obj1._meta.app_label in app_list or obj2._meta.app_label in app_list:
    #         return True
    #     return False