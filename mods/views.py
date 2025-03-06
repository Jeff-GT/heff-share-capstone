from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Mod, Game, ModImage
from .forms import UploadForm, RatingForm
from django.urls import reverse_lazy



class ModListView(ListView):
    template_name = 'mods/mods-list.html'
    model = Mod
    context_object_name = 'mods_list'
    paginate_by = 5

    def get_queryset(self):
        # check for search
        search = self.request.GET.get('search-mod')
        search_data = None
        if search:
            game = self.request.GET.get('game-selector')
            if  game and game != '0':
                # search and game, return filtered
                search_data = Mod.objects.filter(title__icontains=search , game__id=game)            
            else:
                search_data =  Mod.objects.filter(title__icontains=search)

        else:
            game = self.request.GET.get('game-selector')
            if game and game != '0':
                # search and game, return filtered
                search_data = Mod.objects.filter(game__id=game) 
            else:
                    # no search, return all   
                search_data = Mod.objects.all()
        

        # show amount of like a mod has minus the dislikes
        for mod in search_data:
            like = mod.ratings.filter(rating_type='like').count()
            dislike = mod.ratings.filter(rating_type='dislike').count()
            mod.rating = like - dislike
        # Sorting at the bottom
        def sort_by_rating(search_data):
            return -search_data.rating
        mods = sorted(search_data, key=sort_by_rating)  # Ascending order
        return mods
    

    
    def post(self, request, *args, **kwargs):
        # handle rating form
        rating = request.POST['rating'] # like or dislike
        mod_id = request.POST['mod_id']
        mod = Mod.objects.get(id=mod_id)
            
            #create the rating
        mod.ratings.update_or_create(user=request.user, mod=mod, defaults={'rating_type': rating})
        


        return redirect('mods_list')
            

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game_id = self.request.GET.get('game-selector')
        if game_id and game_id != '0':
            context['game'] = Game.objects.get(id=game_id)
        else:
            context['game'] = None
        return context
    



class ModUploadView(CreateView):
    template_name = 'mods/mod-upload.html'
    model = Mod
    form_class = UploadForm
    success_url = reverse_lazy('mods_list')

    def form_valid(self, form):
        mod = form.save(commit=False)
        mod.author = self.request.user
        mod.cover_image = self.request.FILES.get('cover_image')  # Ensure file is properly assigned
        mod.save()
        form.save_m2m()  # Save ManyToMany fields

        images = self.request.FILES.getlist('images')
        for image in images:
            ModImage.objects.create(mod=mod, image=image)
        
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mod_images'] = ModImage.objects.all()  # To display uploaded images
        return context


def upload_mod_images(request, game, pk):
        mod = Mod.objects.get(id=pk)
        
        if request.method == 'POST':
            print(request.FILES)
            
            images = request.FILES.getlist('images')  # Get multiple images

            for image in images:
                ModImage.objects.create(mod=mod, image=image)  # Save each image
            
            return redirect('mod_detail', game=mod.game, pk=mod.id)

        else:
            pass

        return render(request, 'mods/mod-upload.html', {'mod': mod})

        

class ModDetailView(DetailView):
    template_name = 'mods/mod-detail.html'
    model = Mod
    context_object_name = 'mod'

    # load prefretch_related to get all images
    def get_queryset(self):
        return Mod.objects.prefetch_related('images')


    

    def test_func(self):
        Mod = self.get_object()
        if Mod.status.name != "":
            return True
        
