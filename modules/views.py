from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect

from .scrapper import start, get_modules, get_1920_diff_modules
from .models import UndefinedModule, Module
from results.models import ModuleResult
from results.utils import get_or_create_year
from .fix import get_all_modules

@staff_member_required
def start_module_scrape(request):
    get_all_modules()
    return render(request, 'index.html')

@staff_member_required
def update_unknown_modules(request):
    """
    When a Module is created for a user that was missing a module, visit this 
    view to add the newly created module to their profile.
    """
    undefined_modules = UndefinedModule.objects.all()
    undefined_modules_unique = undefined_modules.values_list('module_code', flat=True).distinct()

    created_modules = Module.objects.filter(module_code__in=undefined_modules_unique)
    # for each new module that has been create, add it to the user's profile if 
    # the assessment_groups match. 
    undefined_modules_created = []
    if created_modules.exists():
        for module in created_modules:
            to_add_modules = undefined_modules.filter(module_code=module.module_code)
            if to_add_modules.exists():
                for to_add_module in to_add_modules:
                    assessment_group = module.assessment_groups.filter(
                        assessment_group_code=to_add_module.assessment_group_code
                    )

                    if assessment_group.exists():
                        year = get_or_create_year(to_add_module.user, to_add_module.year)

                        new_module = ModuleResult.objects.create(
                            user=to_add_module.user,
                            year=year,
                            module=module,
                            assessment_group=assessment_group.first(),
                            academic_year=to_add_module.academic_year
                        )
                        undefined_modules_created.append(new_module)
                        to_add_module.delete()

    return render(request, 'update_unknown_modules.html', {'modules': undefined_modules_created})
