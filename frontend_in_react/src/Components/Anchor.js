import React, { Component } from "react";
import StarRatingComponent from "react-star-rating-component";
import axios from "axios";
import "./voting.css";
class Anchor extends Component {
  state = {
    allData: null,
    rating: null
  };
  componentDidMount() {
    const id = localStorage.getItem("id");
    if (id) {
      axios
        .get(
          `http://ec2-52-66-255-118.ap-south-1.compute.amazonaws.com/api/jcount/${id}`
        )
        .then(res => {
          this.setState({
            rating: res.data
          });
        });
    }
  }

  onStarClick = rating => {
    const id = localStorage.getItem("id");
    if (id) {
      let rate = rating.rating;
      let url = `http://ec2-52-66-255-118.ap-south-1.compute.amazonaws.com/api/jcount/${
        rating.docId
      }/update/`;
      axios
        .patch(url, {
          id: rating.docId,
          userId: rating.userId,
          anchorId: rating.anchorId,
          rate: rate
        })
        .then(res => {
          console.log(res);
          window.location.reload();
        });
    } else {
      window.location.replace("/login");
    }
  };

  componentWillReceiveProps(nextProps) {
    if (nextProps && nextProps.data) {
      this.setState({ allData: nextProps.data.Jlist });
    }
  }

  render() {
    let data = [];
    let rating = [];
    let allData = [];

    if (this.state.allData && this.state.rating) {
      data = this.state.allData;
      rating = this.state.rating;
      data.filter((item, index, array) => {
        rating.find(ritem => {
          if (ritem.anchorId === item.id) {
            return allData.push({
              name: item.name,
              wiki: item.wiki,
              image: item.image,
              total_star: item.total_star,
              total_user: item.total_user,
              anchorId: item.id,
              userId: ritem.userId,
              docId: ritem.id,
              stars: ritem.rate
            });
          }
        });
      });
    }

    return (
      <div>
        <div>
          {this.props.data ? console.log("rating in render", rating) : null}
          {rating !== null
            ? allData.map(
                (
                  {
                    name,
                    wiki,
                    image,
                    total_star,
                    total_user,
                    anchorId,
                    userId,
                    docId,
                    stars
                  },
                  index
                ) => (
                  <div key={index}>
                    <div>
                      <div className="thumbnail">
                        <div className="row">
                          <div className="col-md-3">
                            <img
                              className="img-responsive center"
                              src={image}
                              alt="backmyitem"
                              style={{
                                width: "100%",
                                height: "100%",
                                margin: "0 auto"
                              }}
                            />
                            <br />
                          </div>
                          <div className="col-md-9">
                            <div className="row">
                              <div className="col-md-4">Name</div>
                              <div className="col-md-8">{name}</div>
                            </div>
                            <div className="row">
                              <div className="col-md-4">Rating</div>
                              <div className="col-md-8">
                                {(total_star / total_user)
                                  .toString()
                                  .substring(0, 4)}
                              </div>
                            </div>
                            <div className="row">
                              <div className="col-md-4">wiki</div>
                              <div className="col-md-8">
                                <a href={wiki}>{wiki}</a>
                              </div>
                            </div>
                            <div className="row">
                              <div className="col-md-4">You Rated</div>
                              <div className="col-md-8">
                                <StarRatingComponent
                                  name="rate"
                                  starCount={10}
                                  value={stars}
                                  renderStarIcon={() => (
                                    <span style={{ fontSize: "18px" }}>
                                      <i className="fa fa-star" />
                                    </span>
                                  )}
                                  onStarClick={rating =>
                                    this.onStarClick({
                                      rating,
                                      userId,
                                      anchorId,
                                      docId
                                    })
                                  }
                                />{" "}
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                )
              )
            : null}
        </div>

        {console.log("for unregistered", this.props.data)}
        {this.props &&
        this.props.data &&
        this.props.data.Jlist &&
        this.state.rating === null
          ? this.props.data.Jlist.map((item, index) => (
              <div key={index}>
                <div>
                  <div className="thumbnail">
                    <div className="row">
                      <div className="col-md-3">
                        <img
                          className="img-responsive center"
                          src={item.image}
                          alt="backmyitem"
                          style={{
                            width: "100%",
                            height: "100%",
                            margin: "0 auto"
                          }}
                        />
                        <br />
                      </div>
                      <div className="col-md-9">
                        <div className="row">
                          <div className="col-md-4">Name</div>
                          <div className="col-md-8">{item.name}</div>
                        </div>
                        <div className="row">
                          <div className="col-md-4">Anchors:</div>
                          <div className="col-md-8">{item.wiki}</div>
                        </div>
                        <div className="row">
                          <div className="col-md-4">Rating</div>
                          <div className="col-md-8">
                            {item.total_star / item.total_user}
                          </div>
                        </div>
                        <div className="row">
                          <div className="col-md-4">wiki</div>
                          <div className="col-md-8">
                            <a href={item.wiki}>{item.wiki}</a>
                          </div>
                        </div>
                        <div className="row">
                          <div className="col-md-4">You Rated</div>
                          <div className="col-md-8">
                            <StarRatingComponent
                              name="rate"
                              starCount={10}
                              value={0}
                              renderStarIcon={() => (
                                <span style={{ fontSize: "18px" }}>
                                  <i className="fa fa-star" />
                                </span>
                              )}
                              onStarClick={rating =>
                                this.onStarClick({ rating })
                              }
                            />{" "}
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ))
          : null}
      </div>
    );
  }
}

export default Anchor;