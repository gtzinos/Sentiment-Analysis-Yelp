import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {


  developers = [
    {
      name: "Ilias Karatsin",
      title: "Full Stack Developer",
      photo: "https://scontent.fskg1-1.fna.fbcdn.net/v/t1.0-9/13226931_1233808183350275_6020287782455920427_n.jpg?_nc_cat=0&oh=78d74adeab14cb24b4af5997c6e7d9d6&oe=5B81C380",
      description: "Hello...",
      profiles: [
        {
          id: "git",
          url: ""
        }
      ]
    },
    {
      name: "Marinos Zagotsis",
      title: "Full Stack Developer",
      photo: "https://scontent.fskg1-1.fna.fbcdn.net/v/t31.0-8/13048111_10209441039527662_864103833430926887_o.jpg?_nc_cat=0&oh=c5894f0645922afbfd47479fff410785&oe=5B93BC74",
      description: "Hello...",
      profiles: [
        {
          id: "git",
          url: ""
        }
      ]
    },
    {
      name: "Ilias Karatsin",
      title: "Full Stack Developer",
      photo: "https://scontent.fskg1-1.fna.fbcdn.net/v/t1.0-9/13165870_10206152945047169_2926124721482332118_n.jpg?_nc_cat=0&oh=5fc8d7391a79a5699943be0ef1ee3812&oe=5B8C8D43",
      description: "Hello...",
      profiles: [
        {
          id: "git",
          url: ""
        }
      ]
    },
    {
      name: "George Tzinos",
      title: "Full Stack Developer",
      photo: "/assets/tzinos.png",
      description: "Hello...",
      website: "http://www.geotzinos.com",
      social: "https://www.linkedin.com/in/george-tzinos-8a6110101/"
    }
  ]
  constructor() { }

  ngOnInit() {
  }

}
