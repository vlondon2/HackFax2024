import { Component, Inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { SignInComponent } from './components/sign-in/sign-in.component';
import { HttpClientModule } from '@angular/common/http';
import { UserService } from './services/user.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, HomeComponent, SignInComponent, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'frontend';
  private _transformPercentage: number;

  constructor(@Inject(UserService) private _userService: UserService)
  {
    this._transformPercentage = 0;
  }

  public getStyle() {
    console.log("Changing style");
    console.log("User: ", this._userService.user);
    console.log("_transformPercentage", this._transformPercentage);
    if(this._userService.user && this._transformPercentage === 0)
    {
      console.log("Sliding down");
      this._transformPercentage -= 50;
   
    }
    else if(!this._userService.user && this._transformPercentage === -50)
    {
      console.log("Sliding up");
      this._transformPercentage += 50;
     
    }

  
    return {
              transform:  `translateY(${this._transformPercentage}%)`
           }
    
    
  }



}
