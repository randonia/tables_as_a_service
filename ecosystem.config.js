module.exports = {
  apps: [
    {
      name: 'tablr',
      script: './index.js',
      instances: 1,
      exec_mode: 'fork',
      watch: true,
      env: {
        PORT: 18888,
        NODE_ENV: 'development',
      },
    },
  ],
};
