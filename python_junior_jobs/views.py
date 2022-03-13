from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError
from python_junior_jobs.models import Vacancy, Company, Specialty

def main_view(request):
    queryset_company = Company.objects.all()
    queryset_vacancy = Vacancy.objects.all()
    data_specialty = Specialty.objects.all()
    return render(request, "python_junior_jobs/index.html", context={
                                                                        'data_specialty': data_specialty,
                                                                        'data_company': queryset_company,
                                                                        'data_vacancy': queryset_vacancy,
    })


def all_vacancies_view(request):
    data_all_vac=Vacancy.objects.all()
    return render(request, "python_junior_jobs/all_vacancies.html", context={
                                                                                'data_all_vac': data_all_vac,
    })


def vacancies_view(request):
    return render(request, "python_junior_jobs/vacancies.html", context={})


def specialty_view(request, vacancies_1: str, vacancies_2: str):
    cat_spec = Specialty.objects.get(code=vacancies_2)
    cat_vac = Vacancy.objects.all()
    return render(request, "python_junior_jobs/vacancies.html", context={
                                                                            'cat_spec': cat_spec,
                                                                            'cat_vac': cat_vac,

    })


def companies_view(request, id: int):
    data_company = Company.objects.get(id=id)
    data_vacancy = Vacancy.objects.filter(company_id=id)
    return render(request, "python_junior_jobs/company.html", context={
                                                                        'data_company': data_company,
                                                                        'data_vacancy': data_vacancy,
    })


def vacancy_view(request, id: int):
    queryset_vacancy_num = Vacancy.objects.get(id=id)
    queryset_specialty = Specialty.objects.all()
    queryset_company = Company.objects.all()
    return render(request, "python_junior_jobs/vacancy.html", context={
                                                                        'queryset_vacancy_num': queryset_vacancy_num,
                                                                        'queryset_specialty': queryset_specialty,
                                                                        'queryset_company': queryset_company,
    })


def exit_view(request):
    return render(request, "python_junior_jobs/exit.html", context={})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')


def custom_handler400(request, exception):
    # Call when SuspiciousOperation raised
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    # Call when PermissionDenied raised
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')
