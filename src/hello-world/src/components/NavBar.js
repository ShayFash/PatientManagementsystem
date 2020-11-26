import React from 'react';
import { Link } from 'react-router-dom';

function NavBar(props) {
    return (
        <div className="navBar">
            <Link to="/newnote">
                <button className="navBarButton" onClick={props.onClick}>
                    New Note
                </button>
            </Link>
            <Link>
                <button className="navBarButton" onClick={props.onClick}>
                    Requisition Forms
                </button>
            </Link>
            <Link to="/MDsearch">
                <button className="navBarButton" onClick={props.onClick}>
                    MD Search
                </button>
            </Link>
            <Link>
                <button className="navBarButton" onClick={props.onClick}>
                    Prescription
                </button>
            </Link>
            <div className="horizontalDivider" style={{width: "930px"}}/>
            <Link to='/login'>
                <button className="navBarButton" onClick={props.onClick}>
                    Logout
                </button>
            </Link>
        </div>
    )
}



// class NavBar extends React.Component {
//     render() {
//         return (
//             <div className="navBar">
//                 <Link to="/newnote">
//                     <button className="navBarButton" onClick={this.props.onClick}>
//                         New Note
//                     </button>
//                 </Link>
//                 <Link>
//                     <button className="navBarButton" onClick={this.props.onClick}>
//                         Requisition Forms
//                     </button>
//                 </Link>
//                 <Link to="/MDsearch">
//                     <button className="navBarButton" onClick={this.props.onClick}>
//                         MD Search
//                     </button>
//                 </Link>
//                 <Link>
//                     <button className="navBarButton" onClick={this.props.onClick}>
//                         Prescription
//                     </button>
//                 </Link>
//                 <div className="horizontalDivider" style={{width: "930px"}}/>
//                 <Link to='/login'>
//                     <button className="navBarButton" onClick={this.props.onClick}>
//                         Logout
//                     </button>
//                 </Link>
//             </div>
//         );
//     }
// }

export default NavBar;