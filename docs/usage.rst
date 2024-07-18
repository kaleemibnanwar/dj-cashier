=====
Usage
=====

To use Django Cashier in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_cashier',
        ...
    )

Add Django Cashier's URL patterns:

.. code-block:: python

    import dj_cashier


    urlpatterns = [
        ...
        url(r'^', include(dj_cashier.urls)),
        ...
    ]
