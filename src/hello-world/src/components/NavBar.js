import React from 'react';
import { Link, useHistory } from 'react-router-dom';

function NavBar(props) {
    let history = useHistory();
    function handleChange(event) {
        history.push(`/reqform/${event.target.value}`)
    }
    return (
        <div className="navBar">
            <Link to="/newnote">
                <button className="navBarButton" onClick={props.onClick}>
                    New Note
                </button>
            </Link>
            <select className="navBarButton" onChange={handleChange}>
                <option selected disabled>Requisition Forms</option>
                <option value="bloodwork">Blood Work</option>
                <option value="imaging">Imaging</option>
                <option value="ecg">ECG</option>
            </select>

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
            <div className="horizontalDivider" style={{width: "50%"}}/>
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