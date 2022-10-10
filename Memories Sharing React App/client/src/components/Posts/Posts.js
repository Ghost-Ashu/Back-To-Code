import React from 'react';
import { Grid, CircularProgress } from '@material-ui/core';
import { useSelector } from 'react-redux';

import Post from './Post/Post';
import useStyles from './styles';
import Pagination from '../Pagination';

const Posts = ({ setCurrentId }) => {
  const { posts, isLoading } = useSelector((state) => state.posts);
  const classes = useStyles();

  if (!posts.length && !isLoading) return 'No posts';

  
  // const query = useQuery();
  // const page = query.get('page') || 1;
 

  return (
    
    isLoading ? <CircularProgress /> : (
      <Grid className={classes.container} container alignItems="stretch" spacing={3}>
        {posts?.map((post) => (
          <Grid key={post._id} item xs={12} sm={12} md={4} lg={3}>
            <Post post={post} setCurrentId={setCurrentId} />
          </Grid>
        ))}
        {/* {(!searchQuery && !tags.length) && ( */}
              {/* <Paper className={classes.pagination} elevation={6}>
                <Pagination page={page} />
              </Paper> */}
            {/* // )} */}
      </Grid>
    )
  );
};

export default Posts;
