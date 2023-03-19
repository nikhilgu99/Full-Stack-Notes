import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  API_URL = 'http://localhost:5000/notes'
  title = 'Full Stack Notes';

  inputValue = "";
  loaded: boolean = false;
  notes: string[] = [];

  constructor(private http: HttpClient) { }

  addNote(): void {
    var note = <HTMLInputElement>document.getElementById('noteText');

    if(note.value === ""){
      alert("Empty Note");
      return;
    }else if(this.notes.includes(note.value)){
      alert("Note Already Exists");
    }else{

      var jsonValue = JSON.stringify(note.value);

      this.http.post(this.API_URL,jsonValue).subscribe((data)=> {
        this.notes.push(data.toString());
        this.inputValue = "";
      });
    }
  }

  deleteNote(event: any): void {
    var index: string = event.target.parentNode.id;

    this.http.delete<number>(this.API_URL + '/delete/' + index).subscribe((data) => {
      this.notes.splice(data, 1);
    });
  }

  getNotes(): Observable<any> {
    return this.http.get(this.API_URL, {responseType: 'text'});
  }

  keyPressed(event: KeyboardEvent): void {
    if(event.key === "Enter"){
      this.addNote();
    }
  }

  ngOnInit(): void {
      this.getNotes().subscribe((data) => {
        this.notes = JSON.parse(data);
        this.loaded = true;
    });
  }
}
