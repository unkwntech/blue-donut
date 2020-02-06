import React, { Component } from "react";

import { Container, Row, Col } from "reactstrap";

import Header from "../layout/Header";
import Footer from "../layout/Footer";

import Banner from "./Banner";
import Destinations from "./Destinations";
import Create from "./Create";

export class Planner extends Component {
    render() {
        return (
            <>
                <Header />
                <Banner />
                <Container className="pt-5">
                    <Row>
                        <Col className="col-6">
                            <Destinations />
                        </Col>
                        <Col className="col-6">
                            <Create />
                        </Col>
                    </Row>
                </Container>
                <Footer />
            </>
        );
    }
}

export default Planner;
