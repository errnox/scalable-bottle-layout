% rebase('main.html.tpl', title='Example Template')
<div class="container">
  <div class="row">
    <div class="col col-md-12">
      <h2>Template Example</h2>
    </div>
  </div>

  <div class="row">
    <div class="col col-md-6">
      <p>This is a template example.</p>
    </div>
    <div class="col col-md-6">
      <p>Name: <b>{{name}}</b></p>
      % for i in range(n):
      <p>Color: <b>{{color}}</b></p>
      % end
    </div>
  </div>
</div>
