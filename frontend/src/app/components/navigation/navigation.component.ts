import { Component, EventEmitter, Inject, Output } from '@angular/core';
import { MatIconButton, MatButton } from '@angular/material/button';
import { Router } from '@angular/router';
import { UserService } from 'src/app/services/user.service';


@Component({
  selector: 'navigation',
  standalone: true,
  imports: [MatIconButton, MatButton],
  templateUrl: './navigation.component.html',
  styleUrl: './navigation.component.scss'
})
export class NavigationComponent {

  @Output() public toggleNav: EventEmitter<void> = new EventEmitter<void>();

  constructor(@Inject(Router) private _router: Router, @Inject(UserService) private _userService: UserService){

  }

  public onHome(): void
  {
    console.log("Going home!");
    this.toggleNav.emit();
    setTimeout(() => {
      this._router.navigate(['/home']);
    }, 100)
    
  }

  public onTasks(): void
  {
    console.log("Going tasks!");
    this.toggleNav.emit();
    setTimeout(() => {
      this._router.navigate(['/tasks']);
    }, 100)

  }

  public onSignOut(): void
  {
    console.log("Signing out!");
    this._userService.signUserOut();
    this.toggleNav.emit();
    setTimeout(() => {
      this._router.navigate(['']);
    }, 100)
  }

  public onShop(): void
  {
    console.log("Going to Shop!");
    this.toggleNav.emit();
    setTimeout(() => {
      this._router.navigate(['/shop'])
    }, 100)
  }
}
