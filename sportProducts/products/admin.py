from django.contrib import admin

from .models.availability import *
from .models.brand import *
from .models.category import *
from .models.colour import *
from .models.country import *
from .models.cycle import *
from .models.price import *
from .models.product import *
from .models.season import *
from .models.size import *
from .models.sport import *

admin.site.register(Availability)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Colour)
admin.site.register(Country)
admin.site.register(Cycle)
admin.site.register(Price)
admin.site.register(Product)
admin.site.register(Season)
admin.site.register(Size)
admin.site.register(Sport)