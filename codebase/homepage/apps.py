from django.apps import AppConfig


class HomepageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'homepage'


def get_formatted_results(results):
    returnString = ""
    if len(results)>0:
        for each in results:
            returnString+=f"""<li><a href=""><div class="flex gap-3 content-center justify-center overflow-hidden"><figure><img class="w-12 rounded-lg" src="https://www.svgrepo.com/show/192362/doctor.svg" alt="Album"/></figure><div class=""><p class="font-bold text-lg">{each.user.first_name} {each.user.last_name}</p><div class="flex justify-between"><p class="">Language:<strong>{each.languages}</strong></p>&emsp;&emsp;<p class="">Specialty:<strong>{each.speciality}</strong></p></div></div></div></a></li>"""
    else:
        returnString="""
        <li class="text-center">
            <img class="w-24" src="https://www.svgrepo.com/show/408684/page-document-emoji-empty-no-results-empty-page.svg" alt="">
            <p>No Results Found</p>
        </li>
        """
    return returnString