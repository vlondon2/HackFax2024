import { MatDrawer, MatDrawerContainer, MatDrawerContent } from '@angular/material/sidenav';
import { NavigationComponent } from 'src/app/components/navigation/navigation.component';
import { UserService } from 'src/app/services/user.service';
import { MatButtonModule } from '@angular/material/button';
import { Component, Inject, OnInit, ViewChild } from '@angular/core';
import { MatIcon } from '@angular/material/icon';
import { Cosmetic, User } from 'src/app/API types/user';

@Component({
  selector: 'task-board',
  standalone: true,
  imports: [MatIcon, MatDrawer, MatDrawerContainer, MatDrawerContent, NavigationComponent, MatButtonModule],
  templateUrl: './task-board.component.html',
  styleUrl: './task-board.component.scss'
})
export class ShopComponent implements OnInit{
  public user?: User;
  public cosmetics: Cosmetic[];
  @ViewChild('drawer') public drawer?: MatDrawer;

  constructor(@Inject(UserService) private _userService: UserService)
  {
    this.user = this._userService.user;
    this.cosmetics = [];
  }

  public ngOnInit(): void {
    if(this.user)
    {
      this.cosmetics = this.cosmetics.filter(item => {
        return !this.user?.cosmetics.includes(item);
      })
    }
  }
  public toggleNav(): void {
    console.log("Calling toggleNav!");
    this.drawer?.toggle();
  }

}
