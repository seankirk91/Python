#Album = "Redemption"
#Label = "Top Dawg Ent"
#ProducedBy = 'Vinylz'

def producedBy(Producer):
    Producer = 'Vinylz'
    return Producer

def albumName(Album):
    Album = 'Redemption'
    return Album

def labelName(Label):
    Label = 'Top Dawg Ent'
    return Label

WinProducedBy = 'Who'
ProducerIs = producedBy(WinProducedBy)
print"Win was produced by " + (ProducerIs)

WinAlbumName = 'What'
NameIs = albumName(WinAlbumName)
print"The name of the album is " + (NameIs)

WinLabel = '?'
LabelIs = labelName(WinLabel)
print"Win was produced under " + (LabelIs) + " records."
