import { Component, Inject, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserService } from 'src/app/services/user.service';
import { User } from 'src/app/API types/user';''
import {MatButtonModule} from '@angular/material/button';
import {MatSelectModule} from '@angular/material/select';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatDrawer, MatSidenavModule} from '@angular/material/sidenav';
import { MatIconButton } from '@angular/material/button';
import { MatIcon } from '@angular/material/icon';
import { NavigationComponent } from '../navigation/navigation.component';

@Component({
  selector: 'home',
  standalone: true,
  imports: [CommonModule, NavigationComponent, MatButtonModule, MatSelectModule, MatFormFieldModule, MatSidenavModule, MatIconButton, MatIcon],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  public user?: User;

  @ViewChild('drawer') public drawer?: MatDrawer;

  constructor(@Inject(UserService) private _userService: UserService)
  {
    this.user = this._userService.user;
  }

  public getTree(): string{
    let src = '';
    switch(this.user?.level)
    {
      case 1:
        src='assets/TreeSaplingAndLand.png'
        break;
      case 2:
        src='assets/MediumTree.png'
        break;
      default:
        src='assets/FullTreeAndLandImage.png'
        break;
    }

    return src;
  }

  public getUsername(): string {
    if(this.user)
    {
      return this.user.username;
    }

    return "Undefined";
  }

  

  public toggleNav(): void {
    console.log("Calling toggleNav!");
    this.drawer?.toggle();
  }

  public getUserXPBarStyle() {
    if(this.user)
    {
      let xpPercentage = (this.user.xp / this.user.lvlxp) * 100;

      return {
        width: `${xpPercentage}%`
      }
    }

    return{
      width: '0%'
    }
  }

  public hasLamp(): boolean | undefined {
    if(!this.user)
    {
      return false;
    }

    let cosmetics = this.user.cosmetics;
    let hasLamp = false;

    cosmetics.forEach(cosmetic => {
      if(cosmetic.name === "Lamp Post")
      {
       hasLamp = true;
      }
    })

    return hasLamp;
  }

  public hasLantern(): boolean | undefined {
    if(!this.user)
    {
      return false;
    }

    let cosmetics = this.user.cosmetics;
    let hasLantern = false;

    cosmetics.forEach(cosmetic => {
      if(cosmetic.name === "Lantern")
      {
        hasLantern = true;
      }
    })

    return hasLantern;
  }

  public hasBench(): boolean {
    if(!this.user)
    {
      return false;
    }

    let cosmetics = this.user.cosmetics;
    let hasBench = false;

    cosmetics.forEach(cosmetic => {
      if(cosmetic.name === "Bench")
      {
        hasBench = true;
      }
    })

    return hasBench;
  }

  public hasBook(): boolean | undefined {
    if(!this.user)
    {
      return false;
    }

    let cosmetics = this.user.cosmetics;
    let hasBook = false;

    cosmetics.forEach(cosmetic => {
      if(cosmetic.name === "Book")
      {
        hasBook = true;
      }
    })

    return hasBook;
  }

}
