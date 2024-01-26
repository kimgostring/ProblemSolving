function solution(genres, plays) {
    const genrePlayMap = new Map();
    const genreSongsMap = new Map();

    const len = genres.length;
    for (let num = 0; num < len; num++) {
        const genre = genres[num];
        const play = plays[num];
        
        genrePlayMap.set(genre, (genrePlayMap.get(genre) ?? 0) + play);
        genreSongsMap.set(genre, [...(genreSongsMap.get(genre) ?? []), new Song(num, play)]);
    }
    
    const genreArr = [...genrePlayMap.entries()]
        .sort((a, b) => b[1] - a[1])
        .map((entry) => entry[0]);

    return genreArr
        .map((genre) => Song.sort(genreSongsMap.get(genre)).slice(0, 2))
        .flat()
        .map((song) => song.num);
}

class Song {
    constructor(num, play) {
        this.num = num;
        this.play = play;
    }
    
    static sort(songs) {
        return songs.sort((a, b) => a.compareTo(b));
    }
    
    compareTo(another) {
        if (this.play !== another.play) return another.play - this.play;
        return this.num - another.num;
    }
}