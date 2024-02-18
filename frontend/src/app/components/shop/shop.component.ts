import { MatDrawer, MatDrawerContainer, MatDrawerContent } from '@angular/material/sidenav';
import { NavigationComponent } from 'src/app/components/navigation/navigation.component';
import { UserService } from 'src/app/services/user.service';
import { MatButtonModule } from '@angular/material/button';
import { Component, Inject, OnInit, ViewChild } from '@angular/core';
import { MatIcon } from '@angular/material/icon';
import { Cosmetic, User } from 'src/app/API types/user';

@Component({
  selector: 'shop',
  standalone: true,
  imports: [MatIcon, MatDrawer, MatDrawerContainer, MatDrawerContent, NavigationComponent, MatButtonModule],
  templateUrl: './shop.component.html',
  styleUrl: './shop.component.scss'
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
    this._userService.getShop().subscribe((response) => {
      this.cosmetics = response.availableCosmetics;
    })
  }
  public toggleNav(): void {
    console.log("Calling toggleNav!");
    this.drawer?.toggle();
  }

}
