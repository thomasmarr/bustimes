import React from 'react'
import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <>
    <nav>
      <div className="nav-wrapper purple darken-3">
        <Link to="#" data-target="mobile-demo" className="sidenav-trigger"><i className="material-icons">menu</i></Link>
        <ul id="nav-mobile" className="right hide-on-med-and-down">
          <li><Link to="/">Live Arrivals</Link></li>
          <li><Link to="/history">History</Link></li>
        </ul>
      </div>
    </nav>
    <ul className="sidenav" id="mobile-demo">
      <li className="sidenavlink"><Link to="/">Live Arrivals</Link></li>
      <li className="sidenavlink"><Link to="/history">History</Link></li>
    </ul>
    </>
    )
  }

export default Navbar
  