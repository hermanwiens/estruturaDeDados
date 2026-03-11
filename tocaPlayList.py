from PlayList import PlayList
from Musica import Musica

playlist = PlayList("Manguebeat")

playlist.adicionar_musica(Musica("Maracatu Atômico", 284, "Chico Science"))
playlist.adicionar_musica(Musica("Espírito da Mata", 201, "Mestre Ambrósio"))
playlist.adicionar_musica(Musica("Manguetown", 159, "Os Paralamas do Sucesso"))

playlist.tocar()
