from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# models import
from users.models import Profile
from django.contrib.auth.models import User

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    # Variable con los campos a mostrar en el dashboard.
    list_display = (
        'pk',
        'user',
        'phone_number',
        'website',
        'picture',
    )

    # Variable con los campos que serán links.
    list_display_links = (
        'pk',
        'user',
    )

    # Variable con los campos editables desde dashboard| Nota: No puede haber campos link y editables a la vez.
    list_editable = (
        'phone_number',
        'website',
        'picture',
    )

    # Variable con los campos por los que podemos realizar una busqueda.
    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number',
    )

    # Variable que añade un campo por el cual filtrar los datos.
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),)
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography'),
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )
    readonly_fields = ('created', 'modified')


"""
Une los modelos de usuario y perfil para no tener que crear un usuario para asociarlo con un perfil
"""


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
