import React, { Component } from 'react';
import { Switch, Route, Link } from 'react-router-dom';
import { Navbar, Nav, NavDropdown, FormControl, Form, Button } from 'react-bootstrap';
import Recipe from './components/Recipe';

	class App extends Component {
  		state = {
		recipes: []
	};

	async componentDidMount() {
    	try {
				const res = await fetch('http://127.0.0.1:8000/api/recipes/'); // fetching the data from api, before the page loaded
				const recipes = await res.json();
				// console.log(recipes)
				this.setState({
					recipes
				});
			} catch (e) {
				console.log(e);
			}
		}


	render() {
		return (
			<div>
				<Navbar bg="dark" variant="dark">
					<Navbar.Brand href="#home">Recipe Collections</Navbar.Brand>
					<Nav className="mr-auto">
					<Nav.Link href="#">Home</Nav.Link>
					<Nav.Link href="./recipe">Recipes</Nav.Link>
					<Nav.Link href="#shopping">Shopping</Nav.Link>
					<Nav.Link href="#login">Log In</Nav.Link>
					</Nav>
					<Form inline>
					<FormControl type="text" placeholder="Search" className="mr-sm-2" />
					<Button variant="outline-primary">Search</Button>
					</Form>
				</Navbar>
				<Route exact path='/recipe' component={Recipe}/>
				{/* {this.state.recipes.map(item => (
				<div key={item.id}>
					<h1>{item.title}</h1>
					<span>{item.instructions}</span>
				</div>
				))} */}
		</div>
		);
	}
}

export default App;