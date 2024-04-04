module.exports = {
    devServer: {
      proxy: {
        '/api': {
          target: 'http://34.88.180.160:9000', // Change this to your backend URL
          changeOrigin: true,
          pathRewrite: { '^/api': '' },
        },
      },
    },
  };