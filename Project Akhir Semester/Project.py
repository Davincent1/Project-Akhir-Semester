class player:
    tempCount = 0
    def __init__(self, nama, senjata, armor ):
        self.nama = nama
        self.senjata = senjata
        self.armor = armor
        player.tempCount += 1
    def display( self ):
        print(f"Nama Player : { self.nama }  ")
        print(f"senjata Player : { self.senjata }  ")
        print(f"armor Player : { self.armor }  ")
    def gantiNama( self, newNama ):
        self.nama = newNama

class senjata:
    def __init__(self, nm_senjata):
        self.nm_senjata = nm_senjata
    def useSenjata( self ):
        return self.nm_senjata
class armor:
    def __init__(self, nm_armor):
        self.nm_armor = nm_armor
    def usearmor( self ):
        return self.nm_armor

def main():
    senjataKatana = senjata("Katana")
    senjataBusur = senjata("Busur")
    senjataPalu = senjata("Palu Besi")
    senjataTongkat = senjata("Tongkat Bola Api")

    armorTipe = armor("Titanium")
    armorTipe2 = armor("Besi")
    armorTipe3 = armor("Emas")
    armorTipe4 = armor("Perak")

    newPlayer1 = player( "Steve", senjataBusur.useSenjata(), armorTipe.usearmor() )
    newPlayer1.display()

    newPlayer2 = player("Derek", senjataPalu.useSenjata(), armorTipe2.usearmor() )
    newPlayer2.display()
    
    newPlayer3 = player("Martin", senjataKatana.useSenjata(), armorTipe3.usearmor() )
    newPlayer3.display()
    
    newPlayer4 = player("Timothy", senjataTongkat.useSenjata(), armorTipe4.usearmor() )
    newPlayer4.display()

    print(f"Jumlah Object :  { player.tempCount } ")

if __name__ == "__main__":
    main()
