from VideoPlaylist import Video, PlayListVideos

playlist = PlayListVideos("Aula Animada")

playlist.adicionar_video(Video(
    "Maracatu Atômico",
    "https://www.youtube.com/watch?v=_G63uF288T4&list=RD_G63uF288T4&start_radio=1"
))

playlist.adicionar_video(Video(
    "Espirito da Mata",
    "https://www.youtube.com/watch?v=PxqZyfhQlX8&list=RDPxqZyfhQlX8&start_radio=1"
))

playlist.tocar()
