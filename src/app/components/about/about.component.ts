import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {


  developers = []
  constructor() { }

  ngOnInit() {
    let randomDevs = [{
      name: "Ilias Karatsin",
      title: "Full Stack Developer",
      photo: "/assets/ilias.jpg",
      description: "Hello...",
      website: "",
      social: "",
      email: "mailto:karatsin@csd.auth.gr"
    },
    {
      name: "Anastasios Theodosiou",
      title: "Full Stack Developer",
      photo: "https://media.licdn.com/dms/image/C5103AQHN8Jvu3uDVZQ/profile-displayphoto-shrink_800_800/0?e=1531958400&v=beta&t=VSbVAqQTFYQxUBxGQchjFpDKXrxzU4TTFL-MCrPOXis",
      description: "Hello I am Anastasios Theodosiou! I work as a Front-End Developer.",
      website: "https://about.me/anastasios.theodosiou",
      social: "https://www.linkedin.com/in/anastasios-theodosiou",
      email: "mailto:atheodos@csd.auth.gr"
    },
    {
      name: "Marinos Zagkotsis",
      title: "Full Stack Developer",
      photo: "/assets/zagko.jpg",
      description: "Hello I am Marinos Zagkotsis! Msc Student at Aristotle University Of Thessaloniki.",
      social: "https://gr.linkedin.com/in/marinoszagkotsis",
      email: "mailto:zagkotsis@csd.auth.gr"
    },
    {
      name: "George Tzinos",
      title: "Full Stack Developer",
      photo: "/assets/tzinos.png",
      description: "Hello I am George Tzinos! I work as a Web Developer.",
      website: "http://www.geotzinos.com",
      social: "https://www.linkedin.com/in/george-tzinos-8a6110101/",
      email: "mailto:gtzinosv@csd.auth.gr"
    }];

    for (var i = randomDevs.length - 1; i >= 0; i--) {
      this.developers.push(randomDevs.splice(randomDevs.length * Math.random() | 0, 1)[0]);
    }
  }

}
